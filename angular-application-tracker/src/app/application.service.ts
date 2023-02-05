import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable, tap } from 'rxjs';
import { Application } from './application';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class ApplicationService {

  private applicationURL = 'http://192.168.1.163:5001/';

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) { }

  getApplication(uid: string, appID: string) {
    console.log(appID);
    const key = this.authService.getToken()!;
    console.log(key);
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'appID': appID, 'key': key })
    };
    return this.http.get<Application>(this.applicationURL + uid + '/application', httpOptions);
  }

  newApplication(uid: string, pos: string, compN: string, compI: string, city: string, state: string, count: string, resume: string, cv: string, git: string, notes: string, extras: string, mater: string, appli: string, con: string, result: string, dead: string, appliedOn: string, recent: string, fin: string): Observable<Application> {
    var app = { 'position': pos, 'companyName': compN, 'companyInfo': compI, 'city': city, 'state': state, 'country': count, 'resume': resume, 'cv': cv, 'git': git, 'notes': notes, 'extras': extras, 'materials': mater, 'applied': appli, 'contact': con, 'result': result, 'deadline': dead, 'appliedOn': appliedOn, 'recent': recent, 'finalized': fin };
    const key = this.authService.getToken()!;
    
    console.log(key);
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'key': key })
    };
    return this.http.post<Application>(this.applicationURL + uid + '/application' , app, httpOptions).pipe(tap((app: Application) => console.log(app)));
  }
}
