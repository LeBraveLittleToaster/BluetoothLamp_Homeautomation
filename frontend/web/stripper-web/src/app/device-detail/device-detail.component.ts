import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-device-detail',
  templateUrl: './device-detail.component.html',
  styleUrls: ['./device-detail.component.scss']
})
export class DeviceDetailComponent implements OnInit {

  isTurnedOff = false
  brightness = 0

  constructor() { }

  ngOnInit(): void {
  }

  sliderOnChange(value:number | null) : void{
    this.brightness = value == null ? 0 : value
  }


}
