import { Application } from './application';
import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { catchError, tap } from 'rxjs/operators';
import { Observable, of } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ApplicationService {

  private applicationsURL = 'http://localhost:5001/applications'

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json'
    })
}

  constructor(
    private http: HttpClient,
  ) { }

  getApplications(): Observable<Application[]> {
    return this.http.get<Application[]>(this.applicationsURL).pipe(
        tap(_ => console.log('fetched applicationss', _)), 
        catchError(this.handleError<Application[]>('getApplications', []))
    );
  }

  newApplication(application: Application): Observable<Application> {
    return this.http.post<Application>(this.applicationsURL, application, this.httpOptions).pipe(
      tap((newApplication: Application) => console.log(`new application: ${newApplication.id}, ${newApplication.position} ${newApplication.companyName}`)),
      catchError(this.handleError<Application>('newApplication'))
    )
  }

  updateApplication(application: Application): Observable<Application> {
    return this.http.put<Application>(this.applicationsURL, application, this.httpOptions).pipe(
      tap((updatedApp: Application) => console.log('updated application: ' + updatedApp.id)),
      catchError(this.handleError<Application>('updateApplication'))
    )
  }

  deleteApplication(id: number): Observable<Application> {
    return this.http.delete<Application>(this.applicationsURL, this.httpOptions).pipe(
      tap((deleteApp: Application) => console.log('deleting: ' + deleteApp.id + ' ' + deleteApp.position + ' ' + deleteApp.companyName)),
      catchError(this.handleError<Application>('deleteApplication'))
    )
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}
