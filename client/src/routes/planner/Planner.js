import React, { PropTypes } from 'react';
import withStyles from 'isomorphic-style-loader/lib/withStyles';
import s from './Planner.css';

class Planner extends React.Component {
	static propTypes = {
		title: PropTypes.string.isRequired,
	};

	render() {
		const semesters = [{
			number: 1,
			courses: [{
				name: 'Test',
			}],
		}];
		const requirements = [{
			name: 'Test',
		}];
		return (
			<div className={s.root}>
				<div className={s.container}>
					<h1>{this.props.title}</h1>
					<label htmlFor="school">School</label>
					<input id="school" type="text" />
					<label htmlFor="major">Major</label>
					<input id="major" type="text" />

					<h2>Requirements</h2>
					<ul className={s.requirementList}>
						{requirements.map(requirement => (
							<li>{requirement.name}</li>
						))}
					</ul>

					<div className={s.semesterList}>
						{semesters.map(semester => (
							<div className={s.semester}>
								<h2>Semester #{semester.number}</h2>
								<ul className={s.courseList}>
									{semester.courses.map(course => (
										<li className={s.course}>
											<p>{course.name}</p>
										</li>
									))}
								</ul>
							</div>
						))}
					</div>
				</div>
			</div>
		);
	}
}

export default withStyles(s)(Planner);
