import React from "react";
import './Header.css';
import '@fortawesome/fontawesome-free/css/all.css';

function Header() {
    return (
        <header className="header-area">
            <nav className="main-nav">
                <h1 className="logo">SCHOLAR</h1>
                
                <div className="search-input">
                    <input type="text" placeholder="Type Something" />
                    <i className="fa fa-search"></i>
                </div>
                <ul className="nav">
                    <li><a href="#home" className="active">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#courses">Courses</a></li>
                    <li><a href="#team">Team</a></li>
                    <li><a href="#about">About</a></li>
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
