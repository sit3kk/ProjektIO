import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux'
import { RouterProvider } from 'react-router-dom';
import store from './store'
import router from './router';
import './index.css';
import './bootstrap.min.css';

createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Provider store={store}>
            <RouterProvider router={router} />
        </Provider>
    </React.StrictMode>,
);