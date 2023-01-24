import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { Application } from './application';

@Injectable({
  providedIn: 'root'
})
export class ApplicationService {

  private applicationsURL = 'http://localhost:5001/applications'

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    })
  }

  constructor(
    private http: HttpClient,
  ) { }

  getApplications(): Observable<Application[]> {
    return this.http.get<Application[]>(this.applicationsURL).pipe(tap(_ => console.log('fetched applications')), catchError(this.handleError<Application[]>('getApplications', []))
    );
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}
