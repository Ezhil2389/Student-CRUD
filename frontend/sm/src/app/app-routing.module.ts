import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// Import your components here
import { StudentListComponent } from './student-list/student-list.component';
// Add other components if you have them

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'view-students', component: StudentListComponent },
  // Add other routes as needed
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
