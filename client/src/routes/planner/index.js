import React from 'react';
import Layout from '../../components/Layout';
import Planner from './Planner';

const title = 'Planner';

export default {

	path: '/planner',

	action() {
		return {
			title,
			component: <Layout><Planner title={title} /></Layout>,
		};
	},

};
