import { Component, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { Application } from '../application';
import { ApplicationService } from '../application.service';

@Component({
  selector: 'app-update-application',
  templateUrl: './update-application.component.html',
  styleUrls: ['./update-application.component.css']
})
export class UpdateApplicationComponent {

  @Input() app!: Observable<Application>;
  
  constructor(
    private applicationService: ApplicationService,
    private route: ActivatedRoute,
  ) {}

  ngOnInit(): void {
    this.getApp();
  }

  getApp(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.app = this.applicationService.getSingleApplication(id);
  }

  updateApp(position: string, company: string, city: string, state: string, country: string, compNotes: string,resume: string, coverletter: string, github: string, appNotes: string, extras: string, extraMaterial: string, submitted: string, contact: string, result: string): void {
    this.applicationService.updateApplication({ position, company, city, state, country, compNotes, resume, coverletter, github, appNotes, extras, extraMaterial, submitted, contact, result } as unknown as Application).subscribe()
  }
}
