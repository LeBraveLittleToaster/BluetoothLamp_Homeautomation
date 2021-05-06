import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DeviceListComponent } from './device-list/device-list.component';
import { DeviceDetailComponent } from './device-detail/device-detail.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http'
import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatSliderModule } from '@angular/material/slider'
import { MatTabsModule } from '@angular/material/tabs'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatListModule } from '@angular/material/list'
import { MatIconModule } from '@angular/material/icon'
import { MatToolbarModule } from '@angular/material/toolbar'
import { MatRadioModule } from '@angular/material/radio'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatGridListModule } from '@angular/material/grid-list'
import { MatBottomSheetModule } from '@angular/material/bottom-sheet'
import { FormsModule } from '@angular/forms'; 
import { AngularSvgIconModule } from 'angular-svg-icon';
import { DeviceControlsComponent } from './device-controls/device-controls.component';
import { MoodChooserComponent } from './mood-chooser/mood-chooser.component';


@NgModule({
  declarations: [
    AppComponent,
    DeviceListComponent,
    DeviceDetailComponent,
    DeviceControlsComponent,
    MoodChooserComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatCardModule,
    MatButtonModule,
    MatSliderModule,
    MatTabsModule,
    MatButtonToggleModule,
    MatListModule,
    MatIconModule,
    MatToolbarModule,
    MatRadioModule,
    MatProgressSpinnerModule,
    MatProgressBarModule,
    AngularSvgIconModule.forRoot(),
    MatGridListModule,  
    FormsModule,
    MatBottomSheetModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
