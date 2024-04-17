import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Vacancy } from '../models/vacancy';
import { VacancyService } from '../services/vacancy.service';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.scss']
})
export class VacancyListComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private vacancyService: VacancyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getVacancies();
  }

  getVacancies(): void {
    const companyIdParam = this.route.snapshot.paramMap.get('companyId');
    const companyId = companyIdParam ? +companyIdParam : null;
    if (companyId !== null) {
      this.vacancyService.getVacanciesByCompany(companyId)
        .subscribe(vacancies => this.vacancies = vacancies);
    } else {
      console.error('Company ID is null or undefined.');
    }
  }
}
