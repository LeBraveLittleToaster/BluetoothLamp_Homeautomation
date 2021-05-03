import { style, trigger, state, transition, animate } from '@angular/animations';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import Device from '../api-objects/device';

@Component({
  selector: 'app-device-list',
  templateUrl: './device-list.component.html',
  styleUrls: ['./device-list.component.scss'],
  animations: [
    trigger('fade', [      
      transition(':enter', [
        style({opacity: 0}),
        animate(".5s", style({opacity: 1}))
      ]),
      transition(':leave', [
        animate(".5s", style({opacity: 0}))
      ])
    ]),
    trigger('fade_delayed', [      
      transition(':enter', [
        style({opacity: 0}),
        animate(".5s .5s", style({opacity: 1}))
      ]),
      transition(':leave', [
        animate(".5s .5s", style({opacity: 0}))
      ])
    ])
  ],
})
export class DeviceListComponent implements OnInit {

  devices:Device[] | undefined = undefined
  color:string[] = []
  isDetailOpen:boolean = false
  selectedDevice:Device|undefined = undefined

  constructor(private http:HttpClient, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.devices = this.route.snapshot.data.devices.data
    console.log(this.devices)
  }

  onOnClicked(device:Device){
    console.log("CLICKED")
  }

  selectDevice(device:Device|undefined){
    this.selectedDevice = device
    console.group(this.selectedDevice)
  }

  onSubmitClick(index:number):void{
    console.log("INDEX=" + this.color[index])
    this.http.post("http://localhost:4321/device/" + index + "/mode/set", {
      "color" : this.color[index],
      "mode_id" : 0
    }).subscribe()
  }

}
