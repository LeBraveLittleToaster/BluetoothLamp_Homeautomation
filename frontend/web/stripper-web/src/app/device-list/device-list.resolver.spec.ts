import { TestBed } from '@angular/core/testing';

import { DeviceListResolver } from './device-list.resolver';

describe('DeviceListResolver', () => {
  let resolver: DeviceListResolver;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    resolver = TestBed.inject(DeviceListResolver);
  });

  it('should be created', () => {
    expect(resolver).toBeTruthy();
  });
});
