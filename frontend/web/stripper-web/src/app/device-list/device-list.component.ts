import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import Device from '../api-objects/device';

@Component({
  selector: 'app-device-list',
  templateUrl: './device-list.component.html',
  styleUrls: ['./device-list.component.scss']
})
export class DeviceListComponent implements OnInit {

  devices:Device[] | undefined = undefined
  color:string[] = []

  constructor(private http:HttpClient, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.devices = this.route.snapshot.data.devices.data
  }

  onSubmitClick(index:number):void{
    console.log("INDEX=" + this.color[index])
    this.http.post("http://localhost:4321/device/" + index + "/mode/set", {
      "color" : this.color[index],
      "mode_id" : 0
    }).subscribe()
  }

}
