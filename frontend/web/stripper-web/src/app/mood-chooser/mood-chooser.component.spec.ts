import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoodChooserComponent } from './mood-chooser.component';

describe('MoodChooserComponent', () => {
  let component: MoodChooserComponent;
  let fixture: ComponentFixture<MoodChooserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoodChooserComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MoodChooserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
