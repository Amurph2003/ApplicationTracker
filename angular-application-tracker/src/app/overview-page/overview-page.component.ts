import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
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
  user!: User;

  constructor (
    private overviewService: OverviewService,
    private router: Router,
  ) {
    const data = router.getCurrentNavigation()?.extras?.state?['data']: this.user;
  }

  ngOnInit(): void {
    this.user = data;
      this.getOver()
  }

  getOver(): void {
    const id = Number(this.user.id);
    this.overviewService.getOverview(id).subscribe(app => {
      this.apps=app;
      console.log(this.apps);
      console.log(app)
    });
  }
}
