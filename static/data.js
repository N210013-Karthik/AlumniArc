const alumniData = [
    {
        id: 1,
        image: "https://i.pravatar.cc/300?img=1",
        name: "John Doe",
        degree: "B.Tech Computer Science",
        domain: "Software Development",
        graduationYear: 2020,
        company: "Google",
        skills: ["JavaScript", "Python", "React", "Cloud Computing"],
        achievements: [
            {
                title: "Innovation Award",
                description: "Received Google's Innovation Award for developing a breakthrough ML algorithm",
                year: 2023
            },
            {
                title: "Open Source Contribution",
                description: "Major contributor to TensorFlow, with over 100 accepted pull requests",
                year: 2022
            }
        ],
        location: {
            lat: 37.7749,
            lng: -122.4194,
            address: "San Francisco, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/johndoe",
            twitter: "https://twitter.com/johndoe"
        },
        email: "john.doe@example.com",
        mobile: "+1 (555) 123-4567"
    },
    {
        id: 2,
        image: "https://i.pravatar.cc/300?img=2",
        name: "Jane Smith",
        degree: "M.Tech Data Science",
        domain: "Machine Learning",
        graduationYear: 2021,
        company: "Microsoft",
        skills: ["Machine Learning", "Deep Learning", "Python", "TensorFlow"],
        achievements: [
            {
                title: "Research Publication",
                description: "Published groundbreaking research on AI ethics in Nature",
                year: 2024
            },
            {
                title: "Patent Holder",
                description: "Holds two patents in machine learning optimization techniques",
                year: 2023
            }
        ],
        location: {
            lat: 47.6062,
            lng: -122.3321,
            address: "Seattle, WA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/janesmith",
            twitter: "https://twitter.com/janesmith"
        },
        email: "jane.smith@example.com",
        mobile: "+1 (555) 987-6543"
    },
    {
        id: 3,
        image: "https://i.pravatar.cc/300?img=3",
        name: "Michael Chen",
        degree: "B.Tech Electronics",
        domain: "Hardware Engineering",
        graduationYear: 2019,
        company: "Apple",
        skills: ["Circuit Design", "VLSI", "Embedded Systems", "IoT"],
        achievements: [
            {
                title: "Design Excellence",
                description: "Led the design team for Apple's next-gen chip architecture",
                year: 2024
            },
            {
                title: "Mentor Award",
                description: "Recognized for mentoring 50+ junior engineers in chip design",
                year: 2023
            }
        ],
        location: {
            lat: 37.3382,
            lng: -122.0111,
            address: "Cupertino, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/michaelchen",
            twitter: "https://twitter.com/michaelchen"
        },
        email: "michael.chen@example.com",
        mobile: "+1 (555) 234-5678"
    },
    {
        id: 4,
        image: "https://i.pravatar.cc/300?img=4",
        name: "Sarah Johnson",
        degree: "M.Tech Artificial Intelligence",
        domain: "AI Research",
        graduationYear: 2022,
        company: "DeepMind",
        skills: ["Neural Networks", "Computer Vision", "PyTorch", "Research"],
        achievements: [
            {
                title: "AI Breakthrough",
                description: "Developed new reinforcement learning algorithm for robotics",
                year: 2024
            },
            {
                title: "Conference Speaker",
                description: "Keynote speaker at NeurIPS and ICML conferences",
                year: 2023
            }
        ],
        location: {
            lat: 51.5074,
            lng: -0.1278,
            address: "London, UK"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/sarahjohnson",
            twitter: "https://twitter.com/sarahjohnson"
        },
        email: "sarah.johnson@example.com",
        mobile: "+44 20 7123 4567"
    },
    {
        id: 5,
        image: "https://i.pravatar.cc/300?img=5",
        name: "Raj Patel",
        degree: "B.Tech Mechanical",
        domain: "Robotics",
        graduationYear: 2020,
        company: "Boston Dynamics",
        skills: ["Robotics", "ROS", "Python", "Control Systems"],
        achievements: [
            {
                title: "Robotics Innovation",
                description: "Pioneered new walking algorithm for quadruped robots",
                year: 2024
            },
            {
                title: "Tech Award",
                description: "Received IEEE Robotics Innovation Award",
                year: 2023
            }
        ],
        location: {
            lat: 42.3601,
            lng: -71.0589,
            address: "Boston, MA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/rajpatel",
            twitter: "https://twitter.com/rajpatel"
        },
        email: "raj.patel@example.com",
        mobile: "+1 (555) 345-6789"
    },
    {
        id: 6,
        image: "https://i.pravatar.cc/300?img=6",
        name: "Emma Wilson",
        degree: "B.Tech Information Technology",
        domain: "Cybersecurity",
        graduationYear: 2021,
        company: "FireEye",
        skills: ["Network Security", "Ethical Hacking", "Cryptography", "SIEM"],
        achievements: [
            {
                title: "Security Award",
                description: "Received FireEye's Security Award for outstanding contributions",
                year: 2024
            },
            {
                title: "Certified Ethical Hacker",
                description: "Certified as an Ethical Hacker by EC-Council",
                year: 2023
            }
        ],
        location: {
            lat: 37.3688,
            lng: -122.0363,
            address: "Mountain View, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/emmawilson",
            twitter: "https://twitter.com/emmawilson"
        },
        email: "emma.wilson@example.com",
        mobile: "+1 (555) 456-7890"
    },
    {
        id: 7,
        image: "https://i.pravatar.cc/300?img=7",
        name: "Carlos Rodriguez",
        degree: "M.Tech Cloud Computing",
        domain: "DevOps",
        graduationYear: 2020,
        company: "Amazon AWS",
        skills: ["AWS", "Docker", "Kubernetes", "CI/CD"],
        achievements: [
            {
                title: "Cloud Innovation",
                description: "Developed innovative cloud-based solution for AWS customers",
                year: 2024
            },
            {
                title: "AWS Certified",
                description: "Certified as an AWS Solutions Architect",
                year: 2023
            }
        ],
        location: {
            lat: 47.6205,
            lng: -122.3493,
            address: "Seattle, WA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/carlosrodriguez",
            twitter: "https://twitter.com/carlosrodriguez"
        },
        email: "carlos.rodriguez@example.com",
        mobile: "+1 (555) 567-8901"
    },
    {
        id: 8,
        image: "https://i.pravatar.cc/300?img=8",
        name: "Priya Sharma",
        degree: "B.Tech Computer Science",
        domain: "Mobile Development",
        graduationYear: 2022,
        company: "Meta",
        skills: ["React Native", "iOS", "Android", "Mobile Architecture"],
        achievements: [
            {
                title: "Mobile Innovation",
                description: "Developed innovative mobile app for Meta customers",
                year: 2024
            },
            {
                title: "Google Play Award",
                description: "Received Google Play Award for outstanding mobile app development",
                year: 2023
            }
        ],
        location: {
            lat: 37.4848,
            lng: -122.1483,
            address: "Menlo Park, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/priyasharma",
            twitter: "https://twitter.com/priyasharma"
        },
        email: "priya.sharma@example.com",
        mobile: "+1 (555) 678-9012"
    },
    {
        id: 9,
        image: "https://i.pravatar.cc/300?img=9",
        name: "David Kim",
        degree: "M.Tech Data Engineering",
        domain: "Big Data",
        graduationYear: 2021,
        company: "Snowflake",
        skills: ["Apache Spark", "Hadoop", "SQL", "Data Warehousing"],
        achievements: [
            {
                title: "Data Innovation",
                description: "Developed innovative data engineering solution for Snowflake customers",
                year: 2024
            },
            {
                title: "Certified Data Engineer",
                description: "Certified as a Data Engineer by Snowflake",
                year: 2023
            }
        ],
        location: {
            lat: 37.3861,
            lng: -122.0839,
            address: "San Mateo, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/davidkim",
            twitter: "https://twitter.com/davidkim"
        },
        email: "david.kim@example.com",
        mobile: "+1 (555) 789-0123"
    },
    {
        id: 10,
        image: "https://i.pravatar.cc/300?img=10",
        name: "Lisa Wang",
        degree: "B.Tech Electronics",
        domain: "Quantum Computing",
        graduationYear: 2023,
        company: "IBM Quantum",
        skills: ["Quantum Algorithms", "Qiskit", "Python", "Linear Algebra"],
        achievements: [
            {
                title: "Quantum Innovation",
                description: "Developed innovative quantum algorithm for IBM Quantum customers",
                year: 2024
            },
            {
                title: "Quantum Certified",
                description: "Certified as a Quantum Developer by IBM Quantum",
                year: 2023
            }
        ],
        location: {
            lat: 41.1146,
            lng: -73.7191,
            address: "Yorktown Heights, NY"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/lisawang",
            twitter: "https://twitter.com/lisawang"
        },
        email: "lisa.wang@example.com",
        mobile: "+1 (555) 890-1234"
    },
    {
        id: 11,
        image: "https://i.pravatar.cc/300?img=11",
        name: "Tom Anderson",
        degree: "B.Tech Computer Science",
        domain: "Game Development",
        graduationYear: 2020,
        company: "Unity Technologies",
        skills: ["Unity3D", "C#", "Game Design", "3D Modeling"],
        achievements: [
            {
                title: "Game Innovation",
                description: "Developed innovative game engine for Unity Technologies customers",
                year: 2024
            },
            {
                title: "Unity Certified",
                description: "Certified as a Unity Developer by Unity Technologies",
                year: 2023
            }
        ],
        location: {
            lat: 37.7749,
            lng: -122.4194,
            address: "San Francisco, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/tomanderson",
            twitter: "https://twitter.com/tomanderson"
        },
        email: "tom.anderson@example.com",
        mobile: "+1 (555) 901-2345"
    },
    {
        id: 12,
        image: "https://i.pravatar.cc/300?img=12",
        name: "Maria Garcia",
        degree: "M.Tech IoT",
        domain: "Internet of Things",
        graduationYear: 2022,
        company: "Intel",
        skills: ["IoT Protocols", "Embedded C", "MQTT", "Sensor Networks"],
        achievements: [
            {
                title: "IoT Innovation",
                description: "Developed innovative IoT solution for Intel customers",
                year: 2024
            },
            {
                title: "Intel Certified",
                description: "Certified as an IoT Developer by Intel",
                year: 2023
            }
        ],
        location: {
            lat: 45.5155,
            lng: -122.6789,
            address: "Portland, OR"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/mariagarcia",
            twitter: "https://twitter.com/mariagarcia"
        },
        email: "maria.garcia@example.com",
        mobile: "+1 (555) 012-3456"
    },
    {
        id: 13,
        image: "https://i.pravatar.cc/300?img=13",
        name: "Alex Thompson",
        degree: "B.Tech Information Technology",
        domain: "Blockchain",
        graduationYear: 2021,
        company: "Coinbase",
        skills: ["Blockchain", "Smart Contracts", "Solidity", "Web3"],
        achievements: [
            {
                title: "Blockchain Innovation",
                description: "Developed innovative blockchain solution for Coinbase customers",
                year: 2024
            },
            {
                title: "Blockchain Certified",
                description: "Certified as a Blockchain Developer by Coinbase",
                year: 2023
            }
        ],
        location: {
            lat: 37.7903,
            lng: -122.4019,
            address: "San Francisco, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/alexthompson",
            twitter: "https://twitter.com/alexthompson"
        },
        email: "alex.thompson@example.com",
        mobile: "+1 (555) 123-4567"
    },
    {
        id: 14,
        image: "https://i.pravatar.cc/300?img=14",
        name: "Sophie Martin",
        degree: "M.Tech UX Design",
        domain: "User Experience",
        graduationYear: 2023,
        company: "Airbnb",
        skills: ["UI/UX Design", "Figma", "User Research", "Prototyping"],
        achievements: [
            {
                title: "UX Innovation",
                description: "Developed innovative UX solution for Airbnb customers",
                year: 2024
            },
            {
                title: "UX Certified",
                description: "Certified as a UX Designer by Airbnb",
                year: 2023
            }
        ],
        location: {
            lat: 37.7749,
            lng: -122.4194,
            address: "San Francisco, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/sophiemartin",
            twitter: "https://twitter.com/sophiemartin"
        },
        email: "sophie.martin@example.com",
        mobile: "+1 (555) 234-5678"
    },
    {
        id: 15,
        image: "https://i.pravatar.cc/300?img=15",
        name: "James Wilson",
        degree: "B.Tech Mechanical",
        domain: "3D Printing",
        graduationYear: 2022,
        company: "SpaceX",
        skills: ["CAD", "3D Printing", "Material Science", "AutoCAD"],
        achievements: [
            {
                title: "3D Printing Innovation",
                description: "Developed innovative 3D printing solution for SpaceX customers",
                year: 2024
            },
            {
                title: "3D Printing Certified",
                description: "Certified as a 3D Printing Engineer by SpaceX",
                year: 2023
            }
        ],
        location: {
            lat: 33.9207,
            lng: -118.3278,
            address: "Hawthorne, CA"
        },
        socialMedia: {
            linkedin: "https://linkedin.com/in/jameswilson",
            twitter: "https://twitter.com/jameswilson"
        },
        email: "james.wilson@example.com",
        mobile: "+1 (555) 345-6789"
    }
];
