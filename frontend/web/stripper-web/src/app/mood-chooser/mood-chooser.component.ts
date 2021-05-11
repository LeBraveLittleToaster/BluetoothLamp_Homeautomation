import { HttpClient } from '@angular/common/http';
import { Component, Inject, Input, OnInit } from '@angular/core';
import { MatBottomSheetRef, MAT_BOTTOM_SHEET_DATA } from '@angular/material/bottom-sheet';
import Mood from '../api-objects/Mood';
import { MoodBottomSheetData } from '../device-list/device-list.component';

@Component({
  selector: 'app-mood-chooser',
  templateUrl: './mood-chooser.component.html',
  styleUrls: ['./mood-chooser.component.scss']
})
export class MoodChooserComponent implements OnInit {

  constructor(@Inject(MAT_BOTTOM_SHEET_DATA) public moods:Mood[], 
  private _bottomSheetRef: MatBottomSheetRef<MoodChooserComponent>,
  private http:HttpClient) { }

  ngOnInit(): void {
    console.log(this.moods)
  }

  onMoodChanged(mood:Mood){
    this.http.post("http://localhost:4321/moods/set", {
      //"mode" : mood.mode
    }).subscribe();
  }

  onMoodChosen(event:MouseEvent, mood:Mood){
    this.onMoodChanged(mood)
    this._bottomSheetRef.dismiss()
    event?.preventDefault()
  }

}
