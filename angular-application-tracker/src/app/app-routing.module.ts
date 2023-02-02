import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router'
import { AuthGuard } from './auth.guard';
import { LoginComponent } from './login/login.component';
import { OverviewPageComponent } from './overview-page/overview-page.component';

const routes: Routes = [
  { path: '', component: OverviewPageComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
