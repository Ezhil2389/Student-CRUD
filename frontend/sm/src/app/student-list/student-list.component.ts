import { Component, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Student } from '../student.model';
import { StudentService } from '../student.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent {
  showTable: boolean = false;
  students: Student[] = [];
  @Input() SearchFilter: string = '';
  baseUrl = 'http://localhost:5000'; // Update the base URL to your backend's URL

  constructor(private http: HttpClient,
    private studentService: StudentService) {}

  get filteredStudents(): Student[] {
    return this.students.filter((student: Student) =>
      student.name.toLowerCase().includes(this.SearchFilter.toLowerCase()) ||
      student.selectedClass.toLowerCase().includes(this.SearchFilter.toLowerCase())||
      student.rollNumber.toLowerCase().includes(this.SearchFilter.toLowerCase())
    );
  }

  onViewStudentsClick(): void {
    this.http.get<Student[]>(`${this.baseUrl}/view-students`).subscribe(
      (response: Student[]) => {
        this.students = response;
        this.showTable = true;
      },
      (error: any) => {
        console.error('Error fetching students:', error);
        // You can handle the error here, e.g., display an error message to the user
      }
    );
  }
  deleteStudent(student: Student): void {
    const confirmation = confirm(`Are you sure you want to delete ${student.name}?`);
    if (confirmation) {
      this.studentService.deleteStudent(student.rollNumber).subscribe(
        (response: any) => {
          console.log('Student deleted successfully:', response);
          // After successful deletion, refresh the student list
          this.onViewStudentsClick();
        },
        (error: any) => {
          console.error('Error deleting student:', error);
          // You can handle the error here, e.g., display an error message to the user
        }
      );
    }
  }
}
