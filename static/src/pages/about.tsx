// src/pages/About.tsx
import { Link, usePage } from "@inertiajs/react";
import { PageProps as InertiaPageProps } from "@inertiajs/core";

interface AboutProps extends InertiaPageProps {
  app_name: string;
}

export default function About() {
  const { app_name } = usePage<AboutProps>().props;

  return (
    <div>
      <h1>{app_name}</h1>
      <h1>About Page</h1>
      <Link href="/">Back to Home</Link>
    </div>
  );
}
