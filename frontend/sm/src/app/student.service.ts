import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Student } from './student.model';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  private baseUrl = 'http://localhost:5000'; // Update the base URL to your backend's URL

  constructor(private http: HttpClient) {}

  addStudent(student: Student): Observable<any> {
    const url = `${this.baseUrl}/add-student`;
    return this.http.post(url, student);
  }

  updateStudent(updatedStudent: Student): Observable<any> {
    const url = `${this.baseUrl}/update-student`;
    return this.http.post(url, updatedStudent);
  }

  deleteStudent(rollNumber: string): Observable<any> {
    const url = `${this.baseUrl}/delete-student/${rollNumber}`;
    return this.http.delete(url);
  }
}
