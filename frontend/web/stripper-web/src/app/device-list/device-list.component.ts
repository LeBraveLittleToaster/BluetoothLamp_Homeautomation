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

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.devices = this.route.snapshot.data.devices.data
  }

  onSubmitClick(index:number):void{
    console.log("INDEX=" + this.color[index])
  }

}
