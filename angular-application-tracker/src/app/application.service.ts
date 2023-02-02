import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
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
}
