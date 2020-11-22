import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SomethingCoolComponent } from './something-cool.component';

describe('SomethingCoolComponent', () => {
  let component: SomethingCoolComponent;
  let fixture: ComponentFixture<SomethingCoolComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SomethingCoolComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SomethingCoolComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
