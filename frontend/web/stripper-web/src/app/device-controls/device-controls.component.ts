import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import Device from '../api-objects/device';

@Component({
  selector: 'app-device-controls',
  templateUrl: './device-controls.component.html',
  styleUrls: ['./device-controls.component.scss']
})
export class DeviceControlsComponent implements OnInit {

  @Input() selectedDevice:Device | undefined;
  @Output() onBack:EventEmitter<any> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  onBackClicked(){
    this.onBack.emit()
  }

}
