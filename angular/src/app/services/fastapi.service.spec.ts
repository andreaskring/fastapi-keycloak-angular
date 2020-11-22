import { TestBed } from '@angular/core/testing';

import { FastapiService } from './fastapi.service';

describe('FastapiService', () => {
  let service: FastapiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FastapiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
