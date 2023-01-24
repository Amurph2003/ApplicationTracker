import { Company } from "./company";
import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { catchError, tap } from 'rxjs/operators';
import { Observable, of } from "rxjs";
import { MessageService } from "./message.service";

@Injectable({
    providedIn: "root"
})

export class CompanyService {

    private companiesURL = 'http://localhost:5001/companies';

    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json'
        })
    }

    constructor(
        private http: HttpClient,
        private messageService: MessageService,
    ) {}

    getCompanies(): Observable<Company[]> {
        return this.http.get<Company[]>(this.companiesURL).pipe(
            tap(_ => console.log('fetched companies')), 
            catchError(this.handleError<Company[]>('getCompanies', []))
        );
    }

    private handleError<T>(operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {
          console.error(error);
          return of(result as T);
        };
      }
}