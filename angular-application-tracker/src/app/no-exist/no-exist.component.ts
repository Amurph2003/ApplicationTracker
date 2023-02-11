import { Location } from '@angular/common';
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-no-exist',
  templateUrl: './no-exist.component.html',
  styleUrls: ['./no-exist.component.css']
})
export class NoExistComponent {

  constructor(
    private location: Location,
  ) {}

  back() {
    this.location.back();
  }

}
