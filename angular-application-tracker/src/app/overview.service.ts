import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { AuthService } from './auth.service';
import { Overview } from './overview';

@Injectable({
  providedIn: 'root'
})
export class OverviewService {

  private overviewURL = 'https://vercel.com/amurph2003/application-tracker/GWTcR7ex69aVe8WnAYX15GUvZhLs/overview/';

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) { }

  getOverview(uid: string) {
    const key = this.authService.getToken()!;
    console.log(key);
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'key': key })};
    return this.http.get<Overview[]>(this.overviewURL + '/' + uid, httpOptions);
  }
}