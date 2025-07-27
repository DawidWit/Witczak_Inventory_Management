import React, { useState } from 'react';
import styles from './Dashboard.module.css';
import { FaPlus, FaSignOutAlt, FaSearch, FaCalendarAlt, FaSortAmountDownAlt, FaDatabase } from 'react-icons/fa';

const Dashboard: React.FC = () => {
    const [activeStatuses, setActiveStatuses] = useState<string[]>(['available', 'low_stock', 'out_of_stock']);

    const options = [
        { value: 'recently_added', label: 'Recently added' },
        { value: 'name_asc', label: 'Name (A-Z)' },
        { value: 'name_desc', label: 'Name (Z-A)' },
        { value: 'highest_quantity', label: 'Highest quantity' },
        { value: 'lowest_quantity', label: 'Lowest quantity' },
    ];

    const [selectedSortOption, setSelectedSortOption] = useState(options[0].value);

    const handleStatusChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { value, checked } = event.target;
        if (checked) {
            setActiveStatuses((prevStatuses) => [...prevStatuses, value]);
        } else {
            setActiveStatuses((prevStatuses) => prevStatuses.filter((status) => status !== value));
        }
    };

    const handleSortChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setSelectedSortOption(event.target.value);
    };

    // const [searchQuery, setSearchQuery] = useState('');
    // const [startDate, setStartDate] = useState('01.01.1900');
    // const [endDate, setEndDate] = useState('25.07.2025');

    return (
        <div className={styles.dashboardContainer}>
            <div className={styles.sidebar}>
                <div className={styles.sidebarHeader}>
                    <FaDatabase color='#2b7349' size='50' />
                    <h2 className={styles.sidebarTitle}>Inventory Management</h2>
                </div>

                <button className={styles.addResourceBtn}>
                    <FaPlus /> ADD NEW RESOURCE
                </button>
                <div className={styles.filterSection}>
                    <h3 className={styles.filterTitle}>Status</h3>
                    <label className={styles.radioAvaliable}>
                        <input
                            type="checkbox"
                            name="status_available"
                            value="available"
                            className={styles.hiddenCheckbox}
                            checked={activeStatuses.includes('available')}
                            onChange={handleStatusChange}
                        />
                        <span className={`${styles.customCheckbox} ${styles.customCheckboxAvailable}`}></span> AVAILABLE
                    </label>
                    <label className={styles.radioLowStock}>
                        <input
                            type="checkbox"
                            name="status_low_stock"
                            value="low_stock"
                            className={styles.hiddenCheckbox}
                            checked={activeStatuses.includes('low_stock')}
                            onChange={handleStatusChange}
                        />
                        <span className={`${styles.customCheckbox} ${styles.customCheckboxLowStock}`}></span> LOW STOCK
                    </label>
                    <label className={styles.radioOutOfStock}>
                        <input
                            type="checkbox"
                            name="status_out_of_stock"
                            value="out_of_stock"
                            className={styles.hiddenCheckbox}
                            checked={activeStatuses.includes('out_of_stock')}
                            onChange={handleStatusChange}
                        />
                        <span className={`${styles.customCheckbox} ${styles.customCheckboxOutOfStock}`}></span> OUT OF STOCK
                    </label>
                </div>
                <div className={styles.filterSection}>
                    <h3 className={styles.filterTitle}>Categories</h3>
                    <p className={styles.categoryItem}>Item category (24)</p>
                    <p className={styles.categoryItem}>Other item category (17)</p>
                    <p className={styles.categoryItem}>Default item category (11)</p>
                    <button className={styles.showMoreBtn}>SHOW MORE</button>
                </div>
                <div className={styles.logoutSection}>
                    <FaSignOutAlt color='#2b7349' />
                    <div style={{ color: '#2b7349' }}>Log out</div>
                </div>
            </div>
            <div className={styles.mainContent}>
                <div className={styles.mainHeader}>
                    <h1 className={styles.greeting}>Hello email@sample.com!</h1>
                    <div className={styles.headerControls}>
                        <div className={styles.searchBox}>
                            <FaSearch color='#2b7349' size='24' />
                            <input type="text" placeholder="Search..." className={styles.searchInput} />
                        </div>
                        <div className={styles.searchFilters}>
                            <div className={styles.dateRange}>
                                <FaCalendarAlt color='#2b7349' size='24' />
                                <input type="text" value="01.01.1900" className={styles.dateInput} readOnly />
                                <span className={styles.dateSeparator}></span>
                                <input type="text" value="25.07.2025" className={styles.dateInput} readOnly />
                            </div>
                            <div className={styles.sortDropdown}>
                                <FaSortAmountDownAlt color='#2b7349' size='24' />
                                <select
                                    className={styles.sortSelect}
                                    value={selectedSortOption}
                                    onChange={handleSortChange}
                                >
                                    {options.map((option) => (
                                        <option key={option.value} value={option.value} className={styles.sortText}>
                                            {option.label}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
                <div className={styles.inventoryList}>
                    <div className={styles.inventoryItem}>
                        <div className={styles.itemDetails}>
                            <h3 className={styles.itemName}>Item name #1</h3>
                            <div className={styles.itemTags}> <p className={styles.itemCategory}>Item category</p>
                                <span className={styles.itemStatusOutOfStock}>Out of stock</span></div>
                        </div>
                        <div className={styles.itemActions}>
                            <span className={styles.ellipsisIcon}>&#x22EE;</span>
                        </div>
                    </div>
                    <div className={styles.inventoryItem}>
                        <div className={styles.itemDetails}>
                            <h3 className={styles.itemName}>Item name #2</h3>
                            <div className={styles.itemTags}> <p className={styles.itemCategory}>Other item category</p>
                                <span className={styles.itemStatusLowStock}>Low stock |<span>    </span> <span className={styles.stockCount}>7</span></span>  </div>
                        </div>
                        <div className={styles.itemActions}>
                            <span className={styles.ellipsisIcon}>&#x22EE;</span>
                        </div>
                    </div>
                    <div className={styles.inventoryItem}>
                        <div className={styles.itemDetails}>
                            <h3 className={styles.itemName}>Item name #3</h3>
                            <div className={styles.itemTags}>  <p className={styles.itemCategory}>Default item category</p>
                                <span className={styles.itemStatusAvailable}>Available |<span className={styles.stockCount}>50</span></span></div>
                        </div>
                        <div className={styles.itemActions}>
                            <span className={styles.ellipsisIcon}>&#x22EE;</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;