import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Application } from '../application';
import { ApplicationService } from '../application.service';
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
    private applicationService: ApplicationService,
    private authService: AuthService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    if (!this.authService.isLoggedIn())
      this.router.navigate(['/login'])
    this.getOver()
    }

  getOver(): void {
    console.log(this.authService.getId());
    const id = this.authService.getId();
    this.overviewService.getOverview(id).subscribe(app => {
      this.apps=app.sort(this.MyCustomSort('position', 'asc'));
      console.log(this.apps);
      console.log(app)
    });
  }

  deleteApp(id: number) {
    const uid = this.authService.getId();
    this.applicationService.deleteApplication(uid, String(id)).subscribe(app => {
      console.log(app);
    });
    setTimeout(() => {
      window.location.reload();
    }, 250);
  }

  MyCustomSort(by: string, order: string = 'asc') {
    return function innerSort(a: any, b: any){
      if (!a.hasOwnProperty(by) || !b.hasOwnProperty(by)) {
        console.log('here');
        return 0;
      }

      const itemA = (typeof a[by] === 'string') ? a[by].toUpperCase() : a[by];
      const itemB = (typeof b[by] === 'string') ? b[by].toUpperCase() : b[by];
      
      let result = 0;
      if (itemA > itemB)
        result =  1;
      else if (itemA < itemB)
        result = -1;
    return (order === 'desc') ? (result * -1): result
    }
  }
}