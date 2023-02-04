import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Application } from '../application';
import { ApplicationService } from '../application.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-edit-app',
  templateUrl: './edit-app.component.html',
  styleUrls: ['./edit-app.component.css']
})
export class EditAppComponent implements OnInit{
  application?: Application;
  route?: string;

  constructor (
    private applicationService: ApplicationService,
    private authService: AuthService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    this.route = String(this.router.url).split('/')[2];
    console.log(this.route != 'new');
    if(this.route != 'new')
      this.getApp(this.route);
    else
      this.newApp();
  }

  getApp(appId: string): void {
    const uid = this.authService.getId();
    console.log(appId);
    this.applicationService.getApplication(uid, appId).subscribe(application => {
      this.application=application;
      console.log(this.application);
      console.log(application)
    });
    
  }

  editApp() {

  }

  newApp() {
    const uid = this.authService.getId();
    console.log(uid);

  }
}
