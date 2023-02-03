import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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

  constructor (
    private applicationService: ApplicationService,
    private authService: AuthService,
    private route: ActivatedRoute,
  ) {}

  ngOnInit(): void {
      this.getApp();
      if (this.application == null)
        this.newApp(); 
  }

  getApp(): void {
    const uid = this.authService.getId();
    const appId = String(this.route.snapshot.paramMap.get('id'));
    console.log(appId);
    this.applicationService.getApplication(uid, appId).subscribe(application => {
      this.application=application;
      console.log(this.application);
      console.log(application)});
  }

  editApp() {

  }

  newApp() {
    
  }
}
