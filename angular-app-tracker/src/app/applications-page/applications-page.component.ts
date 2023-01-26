import { Component, OnInit} from '@angular/core';
import { Observable } from 'rxjs';
import { Application } from '../application';
import { ApplicationService } from '../application.service';

@Component({
  selector: 'app-applications-page',
  templateUrl: './applications-page.component.html',
  styleUrls: ['./applications-page.component.css']
})
export class ApplicationsPageComponent {

  applications: Application[] = [];
  
  constructor(
    private applicationService: ApplicationService,
  ) {}

  ngOnInit(): void {
    this.getApplications()
  }

  getApplications(): void {
    this.applicationService.getApplications().subscribe(appList => this.applications = appList)
  }

  createApplication(): void {
    this.applicationService
  }
}
