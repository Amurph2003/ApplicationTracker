import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ApplicationDetailComponent } from './application-detail/application-detail.component';
import { ApplicationsPageComponent } from './applications-page/applications-page.component';
import { NewApplicationComponent } from './new-application/new-application.component';
import { SignInPageComponent } from './sign-in-page/sign-in-page.component';
import { UpdateApplicationComponent } from './update-application/update-application.component';

const routes: Routes = [
  { path: 'applications', component: ApplicationsPageComponent },
  { path: 'applications/new', component: NewApplicationComponent },
  { path: 'applications/:id/update', component: UpdateApplicationComponent },
  { path: 'applications/:id', component: ApplicationDetailComponent },
  { path: '', redirectTo: '/sign-in', pathMatch: 'full' },
  { path: 'sign-in', component: SignInPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
