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

  save() {
    const uid = this.authService.getId();
    const app = this.application!;
    console.log(app.position);
    this.applicationService.editApplication(uid, String(app.appId), app.position, app.companyName, app.companyInfo, app.city, app.state, app.country, String(app.resume), String(app.coverletter), String(app.github), app.appNotes, String(app.extras), app.materials, String(app.applied), String(app.contact), String(app.result), app.deadline, app.appliedOn, app.recentCommunication, app.finalizedDate).subscribe(app => {
      console.log(app); 
      this.application = app;
    });

    this.router.navigate(['/application/' + String(this.application!.appId)]);
  }

  newApp(pos: string, compN: string, compI: string = '', city: string, state: string, count: string, resume: string, cv: string, git: string, notes: string = '', extras: string, mater: string = '', appli: string, con: string, result: string, dead: string = '', appliedOn: string = '', recent: string = '', fin: string = '') {
    const uid = this.authService.getId();
    console.log(uid);
    this.applicationService.newApplication(uid, pos, compN, compI, city, state, count, resume, cv, git, notes, extras, mater, appli, con, result, dead, appliedOn, recent, fin).subscribe();
    setTimeout(() => {
      this.router.navigate(['']);
    }, 250);
  }
}
