import { style, trigger, state, transition, animate } from '@angular/animations';
import { HttpClient } from '@angular/common/http';
import { Component, Input, OnInit, Output } from '@angular/core';
import { MatBottomSheet, MatBottomSheetRef } from '@angular/material/bottom-sheet';
import { ActivatedRoute } from '@angular/router';
import Device from '../api-objects/device';
import Mood from '../api-objects/Mood'
import { MoodChooserComponent } from '../mood-chooser/mood-chooser.component';


export interface MoodListResponse{
  m_type:string,
  data: Mood[]
}

export interface DeviceListResponse{
  m_type:string,
  data: Device[]
}
7
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
 
  isLoadingDevices: boolean = true;
  devices:Device[] | undefined = undefined;

  isLoadingMoods: boolean = true;
  moods:Mood[] | undefined = undefined;

  color:string[] = []
  isDetailOpen:boolean = false
  selectedDevice:Device|undefined = undefined
  lastSelectedClass:any = undefined;

  constructor(private http:HttpClient, private _bottomSheet: MatBottomSheet) { }

  ngOnInit(): void {
    this.http.get<DeviceListResponse>("http://localhost:4321/device/list").subscribe((e:DeviceListResponse) => {
      this.devices = e.data
      this.isLoadingDevices = false
      console.log(this.devices)
    })
    

    this.http.get<MoodListResponse>("http://localhost:4321/moods/list").subscribe((e:MoodListResponse) => {
      this.moods = e.data
      this.isLoadingMoods = false
      console.log(this.moods)
    })
    
    
  }

  openBottomSheet(): void {
    this._bottomSheet.open(MoodChooserComponent,
      {
        data: this.moods
      });
  }

  
  onSubmitClick(index:number):void{
    console.log("INDEX=" + this.color[index])
    this.http.post("http://localhost:4321/device/" + index + "/mode/set", {
      "color" : this.color[index],
      "mode_id" : 0
    }).subscribe()
  }

}

export interface MoodBottomSheetData {
  moods: Mood[]
}