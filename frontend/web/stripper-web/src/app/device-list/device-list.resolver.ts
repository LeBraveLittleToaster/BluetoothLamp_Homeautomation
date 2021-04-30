import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {
  Router, Resolve,
  RouterStateSnapshot,
  ActivatedRouteSnapshot
} from '@angular/router';
import { Observable, of } from 'rxjs';
import Device from '../api-objects/device';

@Injectable({
  providedIn: 'root'
})
export class DeviceListResolver implements Resolve<DeviceListResponse> {

  constructor(private http: HttpClient){}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<DeviceListResponse> {
    return this.http.get<DeviceListResponse>("http://localhost:4321/device/list")
  }
}

export interface DeviceListResponse{
  m_type:string,
  data: Device[]
}