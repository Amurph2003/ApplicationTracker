import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'
import { ApplicationComponent } from './application/application.component';
import { AuthGuard } from './auth.guard';
import { EditAppComponent } from './edit-app/edit-app.component';
import { LoginComponent } from './login/login.component';
import { NoExistComponent } from './no-exist/no-exist.component';
import { OverviewPageComponent } from './overview-page/overview-page.component';
import { SignupComponent } from './signup/signup.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent},
  { path: '', component: OverviewPageComponent, canActivate: [AuthGuard] },
  { path: 'application/new', component: EditAppComponent, canActivate: [AuthGuard] },
  { path: 'application/:id', component: ApplicationComponent, canActivate: [AuthGuard] },
  { path: 'application/:id/edit', component: EditAppComponent, canActivate: [AuthGuard] },
  { path: '**', component: NoExistComponent },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
