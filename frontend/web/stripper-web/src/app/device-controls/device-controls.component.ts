import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import Device from '../api-objects/device';

@Component({
  selector: 'app-device-controls',
  templateUrl: './device-controls.component.html',
  styleUrls: ['./device-controls.component.scss']
})
export class DeviceControlsComponent implements OnInit {

  @Input() selectedDevices:Device[] | undefined;
  @Output() onBack:EventEmitter<any> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
    
  }

  onFinishChoosing(options:any){
    console.log("ANY")
    console.log(options)
  }

  onBackClicked(){
    this.onBack.emit()
  }

}
