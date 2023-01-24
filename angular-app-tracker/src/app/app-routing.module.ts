import { ApplicationModule, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ApplicationsComponent } from './applications/applications.component';
import { CompaniesPageComponent } from './companies-page/companies-page.component';

const routes: Routes = [
  { path: 'companies', component: CompaniesPageComponent },
  { path: 'applications', component: ApplicationsComponent },
  // { path:}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
