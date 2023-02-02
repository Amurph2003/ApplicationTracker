import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { Overview } from '../overview';
import { OverviewService } from '../overview.service';
import { User } from '../user';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.css']
})
export class OverviewPageComponent implements OnInit{
  apps: Overview[] = [];

  constructor (
    private overviewService: OverviewService,
    private authService: AuthService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.getOver()
  }

  getOver(): void {
    console.log(this.authService.getId());
    const id = this.authService.getId();
    this.overviewService.getOverview(id).subscribe(app => {
      this.apps=app;
      console.log(this.apps);
      console.log(app)
    });
  }
}