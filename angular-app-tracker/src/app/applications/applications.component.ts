import { Component, OnInit } from '@angular/core';
import { Application } from '../application';
import { ApplicationService } from '../application.service';

@Component({
  selector: 'app-applications',
  templateUrl: './applications.component.html',
  styleUrls: ['./applications.component.css']
})
export class ApplicationsComponent implements OnInit {

  applics: Application[] = [];

  constructor(
    private applicationService: ApplicationService,
  ) {}

  ngOnInit(): void {
    this.getApps()
    
  }

  getApps(): void {
    this.applicationService.getApplications()
      .subscribe(applicationList => this.applics = applicationList)
  }
}
