import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { Overview } from './overview';

@Injectable({
  providedIn: 'root'
})
export class OverviewService {

  private overviewURL = 'http://192.168.1.163:5001/overview';

  constructor(
    private http: HttpClient,
  ) { }

  getOverview(uid: string) {
    return this.http.get<Overview[]>(this.overviewURL + '/' + uid);
  }
}