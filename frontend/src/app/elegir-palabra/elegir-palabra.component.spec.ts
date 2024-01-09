import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ElegirPalabraComponent } from './elegir-palabra.component';

describe('ElegirPalabraComponent', () => {
  let component: ElegirPalabraComponent;
  let fixture: ComponentFixture<ElegirPalabraComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ElegirPalabraComponent]
    });
    fixture = TestBed.createComponent(ElegirPalabraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
