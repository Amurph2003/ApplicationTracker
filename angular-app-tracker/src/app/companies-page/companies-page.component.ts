import { Component, OnInit, Input } from '@angular/core';
import { Company } from '../company';
import { CompanyService } from '../company.service';

@Component({
  selector: 'app-companies-page',
  templateUrl: './companies-page.component.html',
  styleUrls: ['./companies-page.component.css']
})
export class CompaniesPageComponent implements OnInit {

  companies: Company[] = [];

  constructor(
    private companyService: CompanyService,

  ) {}

  ngOnInit(): void {
    this.getCompanies()
    
  }

  getCompanies(): void {
    this.companyService.getCompanies()
      .subscribe(companyList => this.companies = companyList)
  }
}
