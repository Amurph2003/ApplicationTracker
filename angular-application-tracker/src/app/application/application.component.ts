import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { Application } from '../application';
import { ApplicationService } from '../application.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-application',
  templateUrl: './application.component.html',
  styleUrls: ['./application.component.css']
})
export class ApplicationComponent implements OnInit {
  application?: Application;

  constructor (
    private applicationService: ApplicationService,
    private authService: AuthService,
    private route: ActivatedRoute,
    private router: Router,
  ) {}

  ngOnInit(): void {
    // console.log(!this.authService.isLoggedIn())
    console.log('he');
    
    console.log('hello');
    this.getApp()
  }

  getApp(): void {
    const uid = this.authService.getId();
    const appId = String(this.route.snapshot.paramMap.get('id'));
    this.applicationService.getApplication(uid, appId).subscribe(application => {
      this.application=application;
      console.log(this.application);
      console.log(application)});
  }

  deleteApp(id: number) {
    const uid = this.authService.getId();
    this.applicationService.deleteApplication(uid, String(id)).subscribe(app => {
      console.log(app);
    });
    setTimeout(() => {
      this.router.navigate(['']);
    }, 250);
  }

  logOut() {
    this.authService.logout();
  }
}
