import { Component } from '@angular/core';
import { Application } from '../application';
import { ApplicationService } from '../application.service';

@Component({
  selector: 'app-new-application',
  templateUrl: './new-application.component.html',
  styleUrls: ['./new-application.component.css']
})
export class NewApplicationComponent {

  constructor(
    private applicationService: ApplicationService,
  ) {}
  
  newApp(position: string, company: string, city: string, state: string, country: string, compNotes: string,resume: string, coverletter: string, github: string, appNotes: string, extras: string, extraMaterial: string, submitted: string, contact: string, result: string): void {
    this.applicationService.newApplication({ position, company, city, state, country, compNotes, resume, coverletter, github, appNotes, extras, extraMaterial, submitted, contact, result } as unknown as Application).subscribe();
  }
}
