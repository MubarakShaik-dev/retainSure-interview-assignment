## Brief Notes About Your Approach
My approach focused on creating a simple, robust, and maintainable solution by adhering to the principles of clean architecture and separation of concerns.

Architecture: The application is split into three main components:

main.py: Handles the API routing and request/response logic using Flask.

storage.py: Manages all data operations. It acts as a single source of truth for the URL data, abstracting the storage mechanism from the main application.


utils.py: Contains helper functions for URL validation and short code generation, keeping the main application logic clean.


Concurrency: To handle concurrent requests properly, all access to the shared, in-memory data store is protected by a threading.Lock. This ensures that operations like creating a new URL or incrementing a click count are atomic, preventing race conditions.


Data Storage: A simple Python dictionary serves as the in-memory database, as requested. The data structure for each entry stores not only the original URL but also the creation timestamp and the click counter, fulfilling the analytics requirement.

Error Handling: The application includes specific error handlers for 400 (Bad Request) and 404 (Not Found) errors. This ensures the API provides clear, JSON-formatted error messages instead of default HTML error pages, which is a best practice for API design.


Testing: The pytest suite covers all core functionality, error cases, and edge cases, such as providing an invalid URL or a missing JSON key. The tests verify status codes, response data, and side effects like click counter increments.import React, { useState, createContext, useContext } from 'react';

// Mock Data
const mockDoctors = [
    {
        id: '1',
        name: 'Dr. Sarah Johnson',
        specialization: 'Cardiologist',
        image: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=400&h=400&fit=crop&crop=face',
        rating: 4.8,
        experience: '15 years',
        location: 'Medical Center Downtown',
        phone: '+1 (555) 123-4567',
        email: 'sarah.johnson@hospital.com',
        available: true,
        availableSlots: ['09:00', '10:30', '14:00', '15:30', '16:00'],
        bio: 'Specialized in cardiovascular medicine with extensive experience in heart disease prevention and treatment.'
    },
    {
        id: '2',
        name: 'Dr. Michael Chen',
        specialization: 'Dermatologist',
        image: 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?w=400&h=400&fit=crop&crop=face',
        rating: 4.9,
        experience: '12 years',
        location: 'Skin Care Clinic',
        phone: '+1 (555) 234-5678',
        email: 'michael.chen@skincare.com',
        available: true,
        availableSlots: ['08:30', '11:00', '13:30', '15:00'],
        bio: 'Expert in medical and cosmetic dermatology, specializing in skin cancer screening and aesthetic procedures.'
    },
    {
        id: '3',
        name: 'Dr. Emily Rodriguez',
        specialization: 'Pediatrician',
        image: 'https://images.unsplash.com/photo-1594824388853-730c1fe64c48?w=400&h=400&fit=crop&crop=face',
        rating: 4.7,
        experience: '10 years',
        location: 'Children\'s Hospital',
        phone: '+1 (555) 345-6789',
        email: 'emily.rodriguez@childhealth.com',
        available: false,
        availableSlots: [],
        bio: 'Dedicated pediatrician focused on comprehensive healthcare for infants, children, and adolescents.'
    },
    {
        id: '4',
        name: 'Dr. James Wilson',
        specialization: 'Orthopedic Surgeon',
        image: 'https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=400&h=400&fit=crop&crop=face',
        rating: 4.6,
        experience: '18 years',
        location: 'Sports Medicine Center',
        phone: '+1 (555) 456-7890',
        email: 'james.wilson@orthopedics.com',
        available: true,
        availableSlots: ['10:00', '14:30', '16:30'],
        bio: 'Specializes in sports injuries, joint replacement, and minimally invasive orthopedic procedures.'
    }
];

// App Context
const AppContext = createContext();

const useAppContext = () => {
    const context = useContext(AppContext);
    if (!context) {
        throw new Error('useAppContext must be used within AppProvider');
    }
    return context;
};

// Custom CSS-in-JS styling (simulating styled-components)
const styles = {
    container: {
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '0 1rem'
    },
    header: {
        background: 'white',
        boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
        borderBottom: '1px solid #e5e7eb',
        padding: '1rem 0'
    },
    headerContent: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
    },
    logo: {
        display: 'flex',
        alignItems: 'center',
        gap: '0.5rem',
        cursor: 'pointer',
        textDecoration: 'none',
        color: 'inherit'
    },
    logoIcon: {
        width: '2rem',
        height: '2rem',
        background: '#2563eb',
        borderRadius: '0.5rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: 'white',
        fontWeight: 'bold'
    },
    logoText: {
        fontSize: '1.25rem',
        fontWeight: 'bold',
        color: '#111827',
        margin: 0
    },
    backButton: {
        background: 'none',
        border: 'none',
        color: '#2563eb',
        fontWeight: '500',
        cursor: 'pointer',
        padding: '0.5rem 1rem',
        borderRadius: '0.375rem',
        transition: 'color 0.2s'
    },
    main: {
        padding: '2rem 0'
    },
    pageTitle: {
        fontSize: '2rem',
        fontWeight: 'bold',
        color: '#111827',
        marginBottom: '0.5rem'
    },
    pageSubtitle: {
        color: '#6b7280',
        marginBottom: '2rem'
    },
    searchContainer: {
        display: 'flex',
        flexDirection: 'column',
        gap: '1rem',
        marginBottom: '2rem'
    },
    searchInput: {
        width: '100%',
        padding: '0.75rem 0.75rem 0.75rem 2.5rem',
        border: '1px solid #d1d5db',
        borderRadius: '0.5rem',
        fontSize: '1rem',
        transition: 'all 0.2s'
    },
    doctorsGrid: {
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
        gap: '1.5rem'
    },
    doctorCard: {
        background: 'white',
        borderRadius: '0.5rem',
        boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
        padding: '1.5rem',
        transition: 'box-shadow 0.2s'
    },
    doctorHeader: {
        display: 'flex',
        alignItems: 'flex-start',
        gap: '1rem',
        marginBottom: '1rem'
    },
    doctorImage: {
        width: '5rem',
        height: '5rem',
        borderRadius: '50%',
        objectFit: 'cover'
    },
    doctorName: {
        fontSize: '1.125rem',
        fontWeight: '600',
        color: '#111827',
        marginBottom: '0.25rem'
    },
    doctorSpecialization: {
        color: '#2563eb',
        fontWeight: '500',
        marginBottom: '0.5rem'
    },
    doctorFooter: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
    },
    availabilityStatus: {
        display: 'flex',
        alignItems: 'center',
        gap: '0.5rem'
    },
    statusDot: (available) => ({
        width: '0.75rem',
        height: '0.75rem',
        borderRadius: '50%',
        background: available ? '#10b981' : '#ef4444'
    }),
    statusText: (available) => ({
        fontSize: '0.875rem',
        fontWeight: '500',
        color: available ? '#059669' : '#dc2626'
    }),
    viewProfileButton: {
        background: '#2563eb',
        color: 'white',
        padding: '0.5rem 1rem',
        border: 'none',
        borderRadius: '0.5rem',
        fontWeight: '500',
        cursor: 'pointer',
        transition: 'background-color 0.2s'
    },
    profileContainer: {
        background: 'white',
        borderRadius: '0.5rem',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
        overflow: 'hidden'
    },
    profileContent: {
        padding: '2rem'
    },
    profileHeader: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '2rem',
        marginBottom: '2rem'
    },
    profileImage: {
        width: '8rem',
        height: '8rem',
        borderRadius: '50%',
        objectFit: 'cover'
    },
    profileName: {
        fontSize: '1.875rem',
        fontWeight: 'bold',
        color: '#111827',
        marginBottom: '0.5rem',
        textAlign: 'center'
    },
    profileSpecialization: {
        fontSize: '1.25rem',
        color: '#2563eb',
        fontWeight: '600',
        marginBottom: '1.5rem',
        textAlign: 'center'
    },
    bookButton: (disabled) => ({
        padding: '0.75rem 2rem',
        background: disabled ? '#d1d5db' : '#2563eb',
        color: disabled ? '#6b7280' : 'white',
        border: 'none',
        borderRadius: '0.5rem',
        fontWeight: '600',
        cursor: disabled ? 'not-allowed' : 'pointer',
        transition: 'background-color 0.2s'
    }),
    bookingForm: {
        background: 'white',
        borderRadius: '0.5rem',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
        padding: '2rem',
        maxWidth: '42rem',
        margin: '0 auto'
    },
    formTitle: {
        fontSize: '1.5rem',
        fontWeight: 'bold',
        color: '#111827',
        marginBottom: '1.5rem'
    },
    formGroup: {
        marginBottom: '1.5rem'
    },
    formLabel: {
        display: 'block',
        fontSize: '0.875rem',
        fontWeight: '500',
        color: '#374151',
        marginBottom: '0.5rem'
    },
    formInput: (error) => ({
        width: '100%',
        padding: '0.75rem',
        border: `1px solid ${error ? '#ef4444' : '#d1d5db'}`,
        borderRadius: '0.5rem',
        fontSize: '1rem',
        transition: 'all 0.2s'
    }),
    errorText: {
        color: '#ef4444',
        fontSize: '0.875rem',
        marginTop: '0.25rem'
    },
    timeSlots: {
        display: 'grid',
        gridTemplateColumns: 'repeat(3, 1fr)',
        gap: '0.5rem'
    },
    timeSlot: (selected) => ({
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '0.75rem',
        border: `2px solid ${selected ? '#2563eb' : '#e5e7eb'}`,
        background: selected ? '#eff6ff' : 'white',
        color: selected ? '#1d4ed8' : '#374151',
        borderRadius: '0.5rem',
        cursor: 'pointer',
        transition: 'all 0.2s',
        fontWeight: '500'
    }),
    formButtons: {
        display: 'flex',
        gap: '1rem',
        paddingTop: '1rem'
    },
    cancelButton: {
        flex: 1,
        padding: '0.75rem 1.5rem',
        border: '1px solid #d1d5db',
        background: 'white',
        color: '#374151',
        borderRadius: '0.5rem',
        fontWeight: '500',
        cursor: 'pointer',
        transition: 'background-color 0.2s'
    },
    submitButton: {
        flex: 1,
        padding: '0.75rem 1.5rem',
        background: '#2563eb',
        color: 'white',
        border: 'none',
        borderRadius: '0.5rem',
        fontWeight: '500',
        cursor: 'pointer',
        transition: 'background-color 0.2s'
    },
    confirmationCard: {
        background: 'white',
        borderRadius: '0.5rem',
        boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
        padding: '2rem',
        textAlign: 'center',
        maxWidth: '42rem',
        margin: '0 auto'
    },
    successIcon: {
        width: '4rem',
        height: '4rem',
        background: '#d1fae5',
        borderRadius: '50%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        margin: '0 auto 1.5rem',
        color: '#059669',
        fontSize: '2rem'
    },
    emptyState: {
        textAlign: 'center',
        padding: '3rem 0',
        color: '#6b7280'
    }
};

// Components
const Header = ({ currentView, setCurrentView }) => (
    <div style={styles.header}>
        <div style={styles.container}>
            <div style={styles.headerContent}>
                <div style={styles.logo} onClick={() => setCurrentView('home')}>
                    <div style={styles.logoIcon}>📅</div>
                    <h1 style={styles.logoText}>HealthBook</h1>
                </div>
                {currentView !== 'home' && (
                    <button 
                        style={styles.backButton} 
                        onClick={() => setCurrentView('home')}
                    >
                        ← Back to Doctors
                    </button>
                )}
            </div>
        </div>
    </div>
);

const DoctorCard = ({ doctor, onViewProfile }) => (
    <div style={styles.doctorCard}>
        <div style={styles.doctorHeader}>
            <img style={styles.doctorImage} src={doctor.image} alt={doctor.name} />
            <div style={{ flex: 1 }}>
                <h3 style={styles.doctorName}>{doctor.name}</h3>
                <p style={styles.doctorSpecialization}>{doctor.specialization}</p>
                <div style={{ fontSize: '0.875rem', color: '#6b7280', marginBottom: '0.25rem' }}>
                    <span>⭐ {doctor.rating}</span>
                    <span style={{ marginLeft: '1rem' }}>{doctor.experience} experience</span>
                </div>
                <div style={{ fontSize: '0.875rem', color: '#6b7280' }}>
                    📍 {doctor.location}
                </div>
            </div>
        </div>
        
        <div style={styles.doctorFooter}>
            <div style={styles.availabilityStatus}>
                <div style={styles.statusDot(doctor.available)}></div>
                <span style={styles.statusText(doctor.available)}>
                    {doctor.available ? 'Available Today' : 'Not Available'}
                </span>
            </div>
            
            <button style={styles.viewProfileButton} onClick={() => onViewProfile(doctor)}>
                View Profile
            </button>
        </div>
    </div>
);

const DoctorsList = () => {
    const { doctors, setSelectedDoctor, setCurrentView } = useAppContext();
    const [searchTerm, setSearchTerm] = useState('');
    const [filterAvailable, setFilterAvailable] = useState(false);

    const filteredDoctors = doctors.filter(doctor => {
        const matchesSearch = doctor.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                             doctor.specialization.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesFilter = !filterAvailable || doctor.available;
        return matchesSearch && matchesFilter;
    });

    const handleViewProfile = (doctor) => {
        setSelectedDoctor(doctor);
        setCurrentView('profile');
    };

    return (
        <div style={styles.main}>
            <div style={styles.container}>
                <h2 style={styles.pageTitle}>Find Your Doctor</h2>
                <p style={styles.pageSubtitle}>Book appointments with our qualified healthcare professionals</p>

                <div style={styles.searchContainer}>
                    <div style={{ position: 'relative', flex: 1 }}>
                        <input
                            style={styles.searchInput}
                            type="text"
                            placeholder="Search doctors or specializations..."
                            value={searchTerm}
                            onChange={(e) => setSearchTerm(e.target.value)}
                        />
                    </div>
                    
                    <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <input
                            type="checkbox"
                            checked={filterAvailable}
                            onChange={(e) => setFilterAvailable(e.target.checked)}
                        />
                        Available only
                    </label>
                </div>

                <div style={styles.doctorsGrid}>
                    {filteredDoctors.map(doctor => (
                        <DoctorCard 
                            key={doctor.id} 
                            doctor={doctor} 
                            onViewProfile={handleViewProfile}
                        />
                    ))}
                </div>

                {filteredDoctors.length === 0 && (
                    <div style={styles.emptyState}>
                        <p>No doctors found matching your criteria.</p>
                    </div>
                )}
            </div>
        </div>
    );
};

const DoctorProfile = () => {
    const { selectedDoctor, setCurrentView } = useAppContext();

    if (!selectedDoctor) return null;

    const handleBookAppointment = () => {
        setCurrentView('booking');
    };

    return (
        <div style={styles.main}>
            <div style={styles.container}>
                <div style={styles.profileContainer}>
                    <div style={styles.profileContent}>
                        <div style={styles.profileHeader}>
                            <img style={styles.profileImage} src={selectedDoctor.image} alt={selectedDoctor.name} />
                            
                            <div>
                                <h1 style={styles.profileName}>{selectedDoctor.name}</h1>
                                <p style={styles.profileSpecialization}>{selectedDoctor.specialization}</p>
                                
                                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '1rem', marginBottom: '1.5rem' }}>
                                    <div>⭐ {selectedDoctor.rating} Rating</div>
                                    <div>👨‍⚕️ {selectedDoctor.experience} Experience</div>
                                    <div>📍 {selectedDoctor.location}</div>
                                    <div>📞 {selectedDoctor.phone}</div>
                                </div>
                                
                                <div style={styles.availabilityStatus}>
                                    <div style={styles.statusDot(selectedDoctor.available)}></div>
                                    <span style={styles.statusText(selectedDoctor.available)}>
                                        {selectedDoctor.available ? 'Available Today' : 'Not Available Today'}
                                    </span>
                                </div>
                            </div>
                        </div>
                        
                        <div style={{ marginTop: '2rem' }}>
                            <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#111827', marginBottom: '0.75rem' }}>About</h3>
                            <p style={{ color: '#6b7280', lineHeight: '1.6' }}>{selectedDoctor.bio}</p>
                        </div>
                        
                        {selectedDoctor.available && selectedDoctor.availableSlots.length > 0 && (
                            <div style={{ marginTop: '2rem' }}>
                                <h3 style={{ fontSize: '1.125rem', fontWeight: '600', color: '#111827', marginBottom: '0.75rem' }}>Available Time Slots Today</h3>
                                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
                                    {selectedDoctor.availableSlots.map((slot, index) => (
                                        <span key={index} style={{
                                            padding: '0.5rem 0.75rem',
                                            background: '#eff6ff',
                                            color: '#2563eb',
                                            borderRadius: '0.5rem',
                                            border: '1px solid #dbeafe',
                                            fontSize: '0.875rem'
                                        }}>{slot}</span>
                                    ))}
                                </div>
                            </div>
                        )}
                        
                        <div style={{ marginTop: '2rem', textAlign: 'center' }}>
                            <button
                                style={styles.bookButton(!selectedDoctor.available)}
                                onClick={handleBookAppointment}
                                disabled={!selectedDoctor.available}
                            >
                                {selectedDoctor.available ? 'Book Appointment' : 'Not Available'}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

const BookingPage = () => {
    const { selectedDoctor, setCurrentView, bookAppointment } = useAppContext();
    const [formData, setFormData] = useState({
        patientName: '',
        patientEmail: '',
        date: '',
        time: ''
    });
    const [errors, setErrors] = useState({});

    if (!selectedDoctor) return null;

    const validateForm = () => {
        const newErrors = {};

        if (!formData.patientName.trim()) {
            newErrors.patientName = 'Patient name is required';
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!formData.patientEmail.trim()) {
            newErrors.patientEmail = 'Email is required';
        } else if (!emailRegex.test(formData.patientEmail)) {
            newErrors.patientEmail = 'Please enter a valid email address';
        }

        if (!formData.date) {
            newErrors.date = 'Date is required';
        }

        if (!formData.time) {
            newErrors.time = 'Time slot is required';
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = () => {
        if (validateForm()) {
            bookAppointment({
                doctorId: selectedDoctor.id,
                patientName: formData.patientName,
                patientEmail: formData.patientEmail,
                date: formData.date,
                time: formData.time
            });
            setCurrentView('confirmation');
        }
    };

    const handleInputChange = (field, value) => {
        setFormData(prev => ({ ...prev, [field]: value }));
        if (errors[field]) {
            setErrors(prev => ({ ...prev, [field]: '' }));
        }
    };

    const today = new Date().toISOString().split('T')[0];

    return (
        <div style={styles.main}>
            <div style={styles.container}>
                <div style={styles.bookingForm}>
                    <h2 style={styles.formTitle}>Book Appointment</h2>
                    
                    <div style={{ background: '#eff6ff', borderRadius: '0.5rem', padding: '1rem', marginBottom: '1.5rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                            <img style={{ width: '3rem', height: '3rem', borderRadius: '50%', objectFit: 'cover' }} 
                                 src={selectedDoctor.image} alt={selectedDoctor.name} />
                            <div>
                                <h3 style={{ fontWeight: '600', color: '#111827' }}>{selectedDoctor.name}</h3>
                                <p style={{ color: '#2563eb' }}>{selectedDoctor.specialization}</p>
                            </div>
                        </div>
                    </div>

                    <div style={styles.formGroup}>
                        <label style={styles.formLabel}>Patient Name *</label>
                        <input
                            style={styles.formInput(errors.patientName)}
                            type="text"
                            value={formData.patientName}
                            onChange={(e) => handleInputChange('patientName', e.target.value)}
                            placeholder="Enter your full name"
                        />
                        {errors.patientName && <p style={styles.errorText}>{errors.patientName}</p>}
                    </div>

                    <div style={styles.formGroup}>
                        <label style={styles.formLabel}>Email Address *</label>
                        <input
                            style={styles.formInput(errors.patientEmail)}
                            type="email"
                            value={formData.patientEmail}
                            onChange={(e) => handleInputChange('patientEmail', e.target.value)}
                            placeholder="Enter your email address"
                        />
                        {errors.patientEmail && <p style={styles.errorText}>{errors.patientEmail}</p>}
                    </div>

                    <div style={styles.formGroup}>
                        <label style={styles.formLabel}>Appointment Date *</label>
                        <input
                            style={styles.formInput(errors.date)}
                            type="date"
                            value={formData.date}
                            onChange={(e) => handleInputChange('date', e.target.value)}
                            min={today}
                        />
                        {errors.date && <p style={styles.errorText}>{errors.date}</p>}
                    </div>

                    <div style={styles.formGroup}>
                        <label style={styles.formLabel}>Available Time Slots *</label>
                        <div style={styles.timeSlots}>
                            {selectedDoctor.availableSlots.map((slot) => (
                                <div
                                    key={slot}
                                    style={styles.timeSlot(formData.time === slot)}
                                    onClick={() => handleInputChange('time', slot)}
                                >
                                    {slot}
                                </div>
                            ))}
                        </div>
                        {errors.time && <p style={styles.errorText}>{errors.time}</p>}
                    </div>

                    <div style={styles.formButtons}>
                        <button style={styles.cancelButton} onClick={() => setCurrentView('profile')}>
                            Cancel
                        </button>
                        <button style={styles.submitButton} onClick={handleSubmit}>
                            Book Appointment
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

const ConfirmationPage = () => {
    const { selectedDoctor, lastBookedAppointment, setCurrentView } = useAppContext();

    if (!selectedDoctor || !lastBookedAppointment) return null;

    return (
        <div style={styles.main}>
            <div style={styles.container}>
                <div style={styles.confirmationCard}>
                    <div style={styles.successIcon}>✓</div>
                    
                    <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#111827', marginBottom: '0.5rem' }}>
                        Appointment Confirmed!
                    </h2>
                    <p style={{ color: '#6b7280', marginBottom: '2rem' }}>
                        Your appointment has been successfully booked.
                    </p>
                    
                    <div style={{ background: '#f9fafb', borderRadius: '0.5rem', padding: '1.5rem', marginBottom: '2rem', textAlign: 'left' }}>
                        <h3 style={{ fontWeight: '600', color: '#111827', marginBottom: '1rem' }}>
                            Appointment Details
                        </h3>
                        
                        <div style={{ marginBottom: '0.75rem' }}>
                            <p style={{ fontWeight: '500', color: '#111827', marginBottom: '0.125rem' }}>Doctor</p>
                            <p style={{ color: '#6b7280' }}>{selectedDoctor.name} - {selectedDoctor.specialization}</p>
                        </div>
                        
                        <div style={{ marginBottom: '0.75rem' }}>
                            <p style={{ fontWeight: '500', color: '#111827', marginBottom: '0.125rem' }}>Patient</p>
                            <p style={{ color: '#6b7280' }}>{lastBookedAppointment.patientName}</p>
                        </div>
                        
                        <div style={{ marginBottom: '0.75rem' }}>
                            <p style={{ fontWeight: '500', color: '#111827', marginBottom: '0.125rem' }}>Email</p>
                            <p style={{ color: '#6b7280' }}>{lastBookedAppointment.patientEmail}</p>
                        </div>
                        
                        <div style={{ marginBottom: '0.75rem' }}>
                            <p style={{ fontWeight: '500', color: '#111827', marginBottom: '0.125rem' }}>Date & Time</p>
                            <p style={{ color: '#6b7280' }}>{lastBookedAppointment.date} at {lastBookedAppointment.time}</p>
                        </div>
                        
                        <div>
                            <p style={{ fontWeight: '500', color: '#111827', marginBottom: '0.125rem' }}>Location</p>
                            <p style={{ color: '#6b7280' }}>{selectedDoctor.location}</p>
                        </div>
                    </div>
                    
                    <div style={{ background: '#eff6ff', border: '1px solid #dbeafe', borderRadius: '0.5rem', padding: '1rem', marginBottom: '2rem' }}>
                        <p style={{ color: '#1e40af', fontSize: '0.875rem' }}>
                            A confirmation email has been sent to <strong>{lastBookedAppointment.patientEmail}</strong>. 
                            Please arrive 15 minutes early for your appointment.
                        </p>
                    </div>
                    
                    <button 
                        style={styles.bookButton(false)}
                        onClick={() => setCurrentView('home')}
                    >
                        Book Another Appointment
                    </button>
                </div>
            </div>
        </div>
    );
};

// App Provider Component
const AppProvider = ({ children }) => {
    const [doctors] = useState(mockDoctors);
    const [appointments, setAppointments] = useState([]);
    const [selectedDoctor, setSelectedDoctor] = useState(null);
    const [currentView, setCurrentView] = useState('home');
    const [lastBookedAppointment, setLastBookedAppointment] = useState(null);

    const bookAppointment = (appointmentData) => {
        const newAppointment = {
            ...appointmentData,
            id: Date.now().toString(),
            status: 'confirmed'
        };
        
        setAppointments(prev => [...prev, newAppointment]);
        setLastBookedAppointment(newAppointment);
    };

    const contextValue = {
        doctors,
        appointments,
        selectedDoctor,
        currentView,
        setSelectedDoctor,
        setCurrentView,
        bookAppointment,
        lastBookedAppointment
    };

    return (
        <AppContext.Provider value={contextValue}>
            {children}
        </AppContext.Provider>
    );
};

// Main App Component
const App = () => {
    return (
        <AppProvider>
            <div style={{ minHeight: '100vh', background: '#f9fafb' }}>
                <HeaderComponent />
                <MainContent />
            </div>
        </AppProvider>
    );
};

const HeaderComponent = () => {
    const { currentView, setCurrentView } = useAppContext();
    
    return <Header currentView={currentView} setCurrentView={setCurrentView} />;
};

const MainContent = () => {
    const { currentView } = useAppContext();

    switch (currentView) {
        case 'home':
            return <DoctorsList />;
        case 'profile':
            return <DoctorProfile />;
        case 'booking':
            return <BookingPage />;
        case 'confirmation':
            return <ConfirmationPage />;
        default:
            return <DoctorsList />;
    }
};

export default App;