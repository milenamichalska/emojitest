import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';

@Injectable()
export class EmojiApi {
    constructor(private http: HttpClient) {}

    getEmojis(query = ''): Observable<any> {
        const url = '/api/emojis/?search=' + query;
        return this.http.get(url);
    }

    getMeals(): Observable<any> {
        const url = '/api/meals';
        return this.http.get(url);
    }

    getMealTimes(): Observable<any> {
        const url = '/api/mealtimes';
        return this.http.get(url);
    }

    postTestEntry(user, emoji, meal, beforeAfter): Observable<any> {
        const url = '/api/test-entries/';
        return this.http.post(url, {user, emoji, meal, beforeAfter});
    }
}
