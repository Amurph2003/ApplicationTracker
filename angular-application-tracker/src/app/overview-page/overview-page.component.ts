import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Overview } from '../overview';
import { OverviewService } from '../overview.service';
import { User } from '../user';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.css']
})
export class OverviewPageComponent {
  apps: Overview[] = [];

  constructor (
    private overviewService: OverviewService,
  ) {}

  getOver(uid: string): void {
    const id = Number(uid);
    this.overviewService.getOverview(id).subscribe(app => {
      this.apps=app;
      console.log(this.apps);
      console.log(app)
    });
  }
}
