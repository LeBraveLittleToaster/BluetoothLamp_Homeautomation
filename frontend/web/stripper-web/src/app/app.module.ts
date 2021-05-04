import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DeviceListComponent } from './device-list/device-list.component';
import { DeviceDetailComponent } from './device-detail/device-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http'
import { DeviceListResolver } from './device-list/device-list.resolver';
import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatSliderModule } from '@angular/material/slider'
import { MatTabsModule } from '@angular/material/tabs'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatListModule } from '@angular/material/list'
import { MatIconModule } from '@angular/material/icon'
import { MatGridListModule } from '@angular/material/grid-list'
import { FormsModule } from '@angular/forms'; 
import { AngularSvgIconModule } from 'angular-svg-icon';
import { ColorPickerModule } from 'ngx-color-picker';
import { DeviceControlsComponent } from './device-controls/device-controls.component';



@NgModule({
  declarations: [
    AppComponent,
    DeviceListComponent,
    DeviceDetailComponent,
    DeviceControlsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatCardModule,
    ColorPickerModule,
    MatButtonModule,
    MatSliderModule,
    MatTabsModule,
    MatButtonToggleModule,
    MatListModule,
    MatIconModule,
    AngularSvgIconModule.forRoot(),
    MatGridListModule,  
    FormsModule
  ],
  providers: [
    DeviceListResolver,


  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
