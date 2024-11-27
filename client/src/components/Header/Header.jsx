import React from "react";
import './Header.css';
import '@fortawesome/fontawesome-free/css/all.css';

function Header() {
    const handleScroll = (id) => {
        if (id === 'home') {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        } else {
            const element = document.getElementById(id);
            if (element) {
                element.scrollIntoView({ behavior: "smooth", block: "start" });
            }
        }
    };

    return (
        <header className="header-area">
            <nav className="main-nav">
                <h1 className="logo">SCHOLAR</h1>
                
                <div className="search-input">
                    <input type="text" placeholder="Type Something" />
                    <i className="fa fa-search"></i>
                </div>
                <ul className="nav">
                    <li>
                        <a href="#home" onClick={() => handleScroll('home')} className="active">
                            Home
                        </a>
                    </li>
                    <li>
                        <a href="#services" onClick={() => handleScroll('services')}>
                            Services
                        </a>
                    </li>
                    <li>
                        <a href="#courses" onClick={() => handleScroll('courses')}>
                            Courses
                        </a>
                    </li>
                    <li>
                        <a href="#team" onClick={() => handleScroll('team')}>
                            Team
                        </a>
                    </li>
                    <li>
                        <a href="#about" onClick={() => handleScroll('about')}>
                            About
                        </a>
                    </li>
                    <li>
                        <a href="#profile" className="profile-icon">
                            <i className="fa fa-user-circle"></i>
                        </a>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
